$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.fixed-action-btn').floatingActionButton();
    $('.collapsible').collapsible();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('select').formSelect();
  });