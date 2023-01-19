from tabnanny import check
from models import Pet, db

db.drop_all()
db.create_all()

Pabs = Pet(name="Pabs", species="dog", photo_url="https://cdn.pixabay.com/photo/2019/04/10/23/51/animal-4118585__340.jpg", age=9, notes="Goes with the flow", available=False)
CoolLuke = Pet(name="Cool Luke", species="bear", photo_url="https://cdn.pixabay.com/photo/2018/04/10/16/59/bear-3308068__340.jpg", age=3, notes="All good in Cool Luke Town", available=False)
CheckMate = Pet(name="CheckMate", species="cat", photo_url="https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492__340.jpg", age=547, notes="Watch out for this one", available=True)
TreeHugger = Pet(name="Tree hugger", species="koala", photo_url="https://cdn.pixabay.com/photo/2011/09/28/23/19/koala-9960__340.jpg", age=13, notes="Who's got that eucalyptus?", available=True)
david = Pet(name="David", species="dog", photo_url="https://cdn.pixabay.com/photo/2016/04/17/10/38/doberman-1334497__340.jpg", age=7, notes="Security", available=True)
Tony = Pet(name="Tony", species="bear", photo_url="https://cdn.pixabay.com/photo/2018/06/30/19/02/panda-3508153__340.jpg", age=7, notes="What's up", available=True)


for pet in [Pabs, CoolLuke, CheckMate, TreeHugger, david, Tony]:
  db.session.add(pet)

db.session.commit()