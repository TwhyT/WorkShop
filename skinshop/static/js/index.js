// jennie redvibe collection
$().ready(function(){
  var i = 0;
  var images = [
    'static/img/redvibe/janered4.png',
    'static/img/jennielipstick.jpg',
  ]
  var image = $('#imageChange')
  image.css('background-image', 'url( static/img/jennielipstick.jpg )')
  setInterval(function(){
      image.fadeOut(500, function(){
      image.css('background-image', 'url(' + images [i++] +')')
      image.fadeIn(500)
    })
    if(i == 2)
      i = 0
  }, 5000)
})

//Text Shop Aqua
$('#aquaShop').hover(function(){
  $(this).text("NOW");
}, function() {
  $(this).text("SHOP");
});

// AQUA
var aquvideo = document.getElementById("aquaVideo");
var aqubtn = document.getElementById("aquaBtn");
function aqua() {
  if (aquvideo.paused) {
    aquvideo.play();
    aqubtn.innerHTML = "ll";
  } else {
    aquvideo.pause();
    aqubtn.innerHTML = "l>";
  }
}

