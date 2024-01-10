/* global $ */
/* Toogle header class */
$(document).ready(function () {
  $('DIV#toggle_header').on('click', function () {
    $('header').toggleClass('red green');
  });
});
