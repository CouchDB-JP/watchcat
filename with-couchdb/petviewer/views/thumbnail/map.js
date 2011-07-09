function(doc) {
    if(doc.photo) {
	    emit(doc.year + doc.mon + doc.mday + doc.hour, doc);
    };
}