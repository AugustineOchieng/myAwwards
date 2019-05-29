$(function () {
  $("#mdb-lightbox-ui").load("mdb-addons/mdb-lightbox-ui.html");
});

(function ($) {
$('.third.circle').circleProgress({
  value: 0.75,
  fill: { gradient: [['#0681c4', .5], ['#4ac5f8', .5]], gradientAngle: Math.PI / 4 }
}).on('circle-animation-progress', function (event, progress, stepValue) {
  $(this).find('strong').text(stepValue.toFixed(2).substr(1));
});
})(jQuery);
