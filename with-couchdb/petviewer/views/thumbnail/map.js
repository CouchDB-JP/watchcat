function(doc) {

    if(doc.type == "photo") {
	    emit(doc.year + doc.mon + doc.mday + doc.hour, doc);
    };
}