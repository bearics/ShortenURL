$(function () {
  'use strict'

  $('[static-toggle="offcanvas"]').on('click', function () {
    $('.offcanvas-collapse').toggleClass('open')
  })
})

function copyButton(clicked_id) {
  var t = document.createElement("textarea");
  document.body.appendChild(t);
  t.value = document.URL + clicked_id;
  alert('Copy "' + t.value + '"');
  t.select();
  document.execCommand('copy');
  document.body.removeChild(t);
}