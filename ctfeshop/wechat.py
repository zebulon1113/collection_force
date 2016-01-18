#coding:utf8
# author:duoduo3369@gmail.com  https://github.com/duoduo369
"""
Weixin OAuth2 backend, docs at:
"""
from requests import HTTPError

from social.backends.oauth import BaseOAuth2
from social.exceptions import AuthCanceled, AuthUnknownError


class WeixinOAuth2(BaseOAuth2):
    """Weixin OAuth authentication backend"""
    name = 'weixin'
    ID_KEY = 'openid'
    AUTHORIZATION_URL = 'https://open.weixin.qq.com/connect/oauth2/authorize'
    ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/sns/oauth2/access_token'
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False
    EXTRA_DATA = [
        ('nickname', 'username'),
        ('headimgurl', 'profile_image_url'),
    ]

    def get_user_details(self, response):
        print 'get_user_details'
        """Return user details from Weixin. API URL is:
        https://api.weixin.qq.com/sns/userinfo
        """
        if self.setting('DOMAIN_AS_USERNAME'):
            username = response.get('domain', '')
        else:
            username = response.get('nickname', '')
        profile_image_url = response.get('headimgurl', '')
        return {'username': username, 'profile_image_url': profile_image_url}

    def user_data(self, access_token, *args, **kwargs):
        print 'user_data'
        data = self.get_json('https://api.weixin.qq.com/sns/userinfo',
                             params={'access_token': access_token,
                                     'openid': kwargs['response']['openid']})
        nickname = data.get('nickname')
        if nickname:
            data['nickname'] = nickname.encode('raw_unicode_escape').decode('utf-8')
        return data

    def auth_url(self):
        print 'auth_url'
        """Return redirect url"""
        print self.strategy.session_get('next', 'asdfasdfasdf')
        appid, secret = self.get_key_and_secret()
        redirect_uri = self.get_redirect_uri().replace(':', '%3a').replace('/', '%2f')
        return '{0}?appid={1}&redirect_uri={2}&response_type=code&scope=snsapi_userinfo&connect_redirect=1#wechat_redirect'.format(self.authorization_url(), appid, redirect_uri)

    def auth_complete_params(self, state=None):
        print 'auth_complete_params'
        appid, secret = self.get_key_and_secret()
        return {
            'grant_type': 'authorization_code',  # request auth code
            'code': self.data.get('code', ''),  # server response code
            'appid': appid,
            'secret': secret,
            'redirect_uri': self.get_redirect_uri()
        }

    def refresh_token_params(self, token, *args, **kwargs):
        print 'refresh_token_params'
        appid, secret = self.get_key_and_secret()
        return {
            'refresh_token': token,
            'grant_type': 'refresh_token',
            'appid': appid,
            'secret': secret
        }

    def auth_complete(self, *args, **kwargs):
        print 'auth_complete'
        """Completes loging process, must return user instance"""
        self.process_error(self.data)
        try:
            response = self.request_access_token(
                self.ACCESS_TOKEN_URL,
                data=self.auth_complete_params(),
                headers=self.auth_headers(),
                method=self.ACCESS_TOKEN_METHOD
            )
        except HTTPError as err:
            if err.response.status_code == 400:
                raise AuthCanceled(self)
            else:
                raise
        except KeyError:
            raise AuthUnknownError(self)
        if 'errcode' in response:
            raise AuthCanceled(self)
        self.process_error(response)
        return self.do_auth(response['access_token'], response=response,
                            *args, **kwargs)
