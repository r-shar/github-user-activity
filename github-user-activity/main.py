from fastapi import FastAPI
from argparse import ArgumentParser

app = FastAPI()

@app.get("/")
async def root(): 
  return {"message": "hello world"}



def main():
  argparser = ArgumentParser(
    prog='git-user-activity',
    description='Lists github user activity',
  )
  
  argparser.add_argument("username")
  args = argparser.parse_args()
  print(f'Github username: {args.username}')
  
main() 
