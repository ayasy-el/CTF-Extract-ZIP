pattern="*.zip"
files=( $pattern )
filename=$files
while [ -f $filename ]; do
  # Proses file *.zip
  var="$(cat password.txt)" && unzip -P $var -o $filename
  echo "Ekstrak $filename"
  rm $filename
  pattern="*.zip"
  files=( $pattern )
  filename=$files
done