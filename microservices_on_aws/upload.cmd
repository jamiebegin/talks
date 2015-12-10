7za a -tzip %1.zip .\%1\*
aws lambda update-function-code ^
--zip-file fileb://%1.zip ^
--function-name %2 ^
--profile %3
del %1.zip