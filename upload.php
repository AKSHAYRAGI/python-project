<?php
if (!empty($_FILES) && isset($_FILES['fileToUpload'])) {
    switch ($_FILES['fileToUpload']["error"]) {
        case UPLOAD_ERR_OK:
            $target = "upload/";
            $target = $target . basename($_FILES['fileToUpload']['name']);
            if (move_uploaded_file($_FILES['fileToUpload']['tmp_name'], $target)) {
                $status = "The file " . basename($_FILES['fileToUpload']['name']) . " has been uploaded";
                $imageFileType = pathinfo($target, PATHINFO_EXTENSION);
                $check = getimagesize($target);
                if ($check !== false) {
                    $command = escapeshellcmd('python medical_records_extraction.py');
                    $output = shell_exec($command);
                    echo "You belong to the cohort : ".$output;

                    $uploadOk = 1;
                } else {
                    echo "File is not an image.<br>";
                    $uploadOk = 0;
                }

            } else {
                $status = "Sorry, there was a problem uploading your file.";
            }
            break;

    }

}