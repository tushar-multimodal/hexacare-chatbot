mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"tush.r1711@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
\n\
[theme]\n\
base = \"light\"\n\
primaryColor = \"#89CFF0\"\n\
backgroundColor = \"#E0F7FE\"\n\
secondaryBackgroundColor = \"#FFFCE4\"\n\
textColor = \"#000000\"\n\
font = \"sans serif\"\n\
" > ~/.streamlit/config.toml
