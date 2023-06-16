$(document).ready(function() { 
  $('#downloadAllButton').click(function() {
    $('a.download_file > mp3').trigger( "click" );

    return false;
  });
});
