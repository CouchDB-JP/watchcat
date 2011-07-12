$(function() {

    function getSearchKey() {
	return $('input#searchkey').val();
    }

    function basename(path) {
	return path.replace(/\\/g,'/').replace( /.*\//, '' );
    }

    function getDocId () {
	return basename(window.location.pathname);
    }

    function getJsonUri() {
	return "../../_view/thumbnail?key=%22" + getSearchKey() + "%22";
    }


    $.getJSON(getJsonUri(),
	      function(data) {

		  var id = [];
		  var nextid = [];
		  var previd = [''];
		  var idlist = new Array();

		  // parse JSON.
		  $.each(data, function(key, val) {

		      if (data.rows) {
			  $.each(val, function(key2, val2) {

			      $.each(val2, function(key3, val3) {

				  if (key3 == "id") {
				      id.push(val3);
				  }
			      });
			  });
		      }
		  });

		  // next id list.
		  nextid = id.slice(0);
		  nextid.shift();
		  nextid.push('');

		  // previous id list.
		  previd = previd.concat(id.slice(0));
		  previd.pop();

		  // Array idlist is [["id", "previd", "nextid"], [],...]
		  for (var i in id) {
		      idlist.push([
			  id[i], 
			  previd[i],
			  nextid[i]
		      ]);
		  }

		  // search previd, nextid by id.
		  for (var i = 0; i < idlist.length; i++) {

		      if (idlist[i][0] == getDocId()) {
			  if (idlist[i][1]) {
			      $('a#prev').attr('href', idlist[i][1]); // previous id button
			  } else {
			      $('a#prev').remove();
			  }
			  if (idlist[i][2]) {
			      $('a#next').attr('href', idlist[i][2]); // next id button
			  } else {
			      $('a#next').remove();
			  }
		      }
		  }

	      });

});

