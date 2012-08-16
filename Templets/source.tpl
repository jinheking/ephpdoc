<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org./TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<link media="screen" href="./css/group.css" type="text/css" rel="Stylesheet" />
	<link media="screen" href="./css/green.css" type="text/css" rel="Stylesheet" />
	<script src="./js/application.js" type="text/javascript"></script>
	<link media="screen" href="./css/SyntaxHighlighter.css" type="text/css" rel="Stylesheet" />
	<script src="./js/shCoreCommon.js" type="text/javascript"></script>
	<link media=screen href="./css/ui.css" type="text/css" rel="Stylesheet" />
	<script src="./js/compress.js" type="text/javascript"></script>
	<meta content="MSHTML 6.00.2900.3268" name="GENERATOR" />		
</head>
<body >

<div align='center' class='title'>
JAVA文件操作类（转载）</div>

<div align="left">

<pre class="python" name="code">

</pre>

</div>

</div>
</div>
<form id="comment_form" onsubmit="return false;" action="" method="post">

</form>
<script type="text/javascript">
	new Validation("comment_form", {immediate: false, onFormValidate: function(result, form){
		if(result) {
			new Ajax.Request('/group/create_blog_comment/171568', {
				onSuccess:function(response){
					Element.scrollTo($('comments'));
					$('comments').insert({after:response.responseText})
					$('editor_body').value = "";
					$('_form_spinner_').hide();
				}, parameters:Form.serialize(form)
			});
		}
	}});
	
	dp.SyntaxHighlighter.HighlightAll('code', true, true);
	fix_image_size($$('div.blog_content img'), 700);
</script>
</body>
</html>
