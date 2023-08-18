# Input file containing usernames and passwords
input_file="user_data.txt"
while IFS= read -r line; do
  username=$(echo "$line" | cut -d " " -f 1)
  password=$(echo "$line" | cut -d " " -f 2)
  useradd -m "$username" -p "$password"
  done < "$input_file"
