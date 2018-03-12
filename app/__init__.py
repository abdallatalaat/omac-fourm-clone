
from flask import Flask, render_template
from app import store, models, dummy_data

app = Flask(__name__)

member_store = store.MemberStore()
post_store = store.PostStore()
dummy_data.seed_stores(member_store, post_store)

from app import views
