<html>
    <head>
	    <title>Signup received</title>
	</head>
	<body>
	    <p>
		    Your information has been recieved.
		</p>
        <?php
            foreach($_REQUEST as $key => $value) {
                echo $key, " = ", $value, "<br />";
            }
        ?>
	</body>
</html>
