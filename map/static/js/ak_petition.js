$(document).ready(function() {
  actionkit.forms.initPage();

  $('#not_in_us').click(function() {
    $('#country_drop_down').show();
    $('#id_zip').parent().hide();
    return false;
  });
  $('#yes_in_us').click(function() {
    $('#country_drop_down').hide();
    $('#id_zip').parent().show();
    return false;
  });

});