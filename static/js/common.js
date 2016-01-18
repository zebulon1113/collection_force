$(document).ready(function(){
	$('.cartoon,.cartoonGif,.cartoonBg,.second1').css({'height':$(window).height(),'width':$(window).width()})
	firstPage();
	$(".container").css('height',$(window).height());
	
	$('.cartoonBtn').click(function(){
		$(".firstPage").css('display','none');
		$(".second1").css('display','block').addClass('fadeIn');
	});
	$('.page2-1').click(function(){
		$('.page2-1-2').css('display','block');
		$('.page2-2-2').css('display','block');
		$('.page2-4').css('display','none');
		$('.page2-5').css('display','block');
		$('.page2-1').css('display','none');
		$('.page2-2').removeClass('flip')
	});
	$('.page2-2-2').click(function(){
		$('.page2-2-2').css('display','none');
		$('.page2-1-2').css('display','none');
		$('.page2-2').css('display','block').addClass('flip')
		$('.page2-4').css('display','block');
		$('.page2-5').css('display','none');
		$('.page2-1').css('display','block');
	});
	var num=0;
	$('.page6-2').click(function(){
		num+=10;
		$('.progress').css('width',num+'%');
	});
	$('.page6-3').click(function(){
		$('.page6-5').css('display','block').removeClass('bounceOut').addClass('bounceIn');
		$('.page5-bg').css('display','block');
	});
	$('.page5-bg').click(function(){
		$('.page5-bg').css('display','none');
	})
	$('.page6-5').click(function(){
		$(this).addClass('bounceOut').css('display','none');
		$('.page5-bg').css('display','none');
	});
	$('.page6-4').click(function(){
		$('.page6-6').css('display','block').removeClass('bounceOut').addClass('bounceIn');
		$('.page5-bg').css('display','block');
	});
	$('.page6-6').click(function(){
		$(this).addClass('bounceOut').css('display','none');
		$('.page5-bg').css('display','none');
	});
	
	$('.music').click(function(){
		if ($('#musicAudio').pause) {
			$('#musicAudio').play();
		}else{
			$('#musicAudio').pause();
		};
	})
});//结束

function firstPage(){
	$(".cartoon").addClass("zoomIn");
	setTimeout(function(){
		$('.cartoon').removeClass('zoomIn').addClass('bounceOut');
	},3000);
	setTimeout(function(){
		$('.cartoonGif').css('display','block');
	},4000);
	setTimeout(function(){
		$('.cartoonGif').addClass('fadeOut');
	},8000);
	setTimeout(function(){
		$('.cartoonBg').css('display','block');
		$('.cartoonBg').addClass('fadeIn');
	},9000);
	setTimeout(function(){
		$('.boat1').css('display','block');
		$('.boat1').addClass('zoomIn');
	},9000);
	setTimeout(function(){
		$('.boat2,.boat4,.boat6,.boat8').css('display','block');
		$('.boat2,.boat4,.boat6,.boat8').addClass('zoomIn');
	},9500);
	setTimeout(function(){
		$('.boat3,.boat9,.boat5,.boat7').css('display','block');
		$('.boat3,.boat9,.boat5,.boat7').addClass('zoomIn');
	},10000);
	setTimeout(function(){
		$('.cartoonTitle').css('display','block');
		$('.cartoonTitle').addClass('zoomIn');
	},11000);
	setTimeout(function(){
		$('.cartoonBtn').css('display','block');
		$('.cartoonBtn').addClass('bounceInUp');
	},11000);
	
};
function playPause() {    
    var music = document.getElementById('music2');    
    var music_btn = document.getElementById('music_btn2');    
    if (music.paused){    
        music.play();    
        music_btn.src = './img/music.png';    
    }    
    else{    
        music.pause();    
        music_btn.src = './img/music1.png';     
    }    
}   
