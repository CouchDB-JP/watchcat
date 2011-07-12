$(function() {

    var key = "2011062223";
    var uri = "https://nekozanmai.net/watchcat-staging/_design/petviewer/_view/thumbnail?key=%22" + key + "%22";
    var keyid = "9afc600e507552f39914ef315c001d21";
    
    $.getJSON(uri, 
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

		      if (idlist[i][0] == keyid) {
			  $('a#prev').attr('href', idlist[i][1]); // previous id button
			  $('a#next').attr('href', idlist[i][2]); // next id button
		      }
		  }
				  
	      });



});

