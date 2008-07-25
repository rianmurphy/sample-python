
function mapUrlToJxpFile( uri , req ){
    if ( uri.match( /^.\w+$/ ) ){
	req.name = uri.substring(1);
	return "/controller.py";
    }
}
