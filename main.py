from website import create_app

app = create_app() #from __init__.py

if __name__ == '__main__': #only if we run this file (not importing)
    app.run(debug=True) #run the flask aplication and start off a web server.debug=true means that every time we make a change in our python code its will rerun the web server.