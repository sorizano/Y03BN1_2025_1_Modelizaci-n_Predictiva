import streamlit as st
import pandas pd
import supabase
import datatime
from supabase import create_client
import json
import secrets

#Configurar el cliente de Supabase
SUPABASE_URL = secrets.SUPABASE_URL
SUPABASE_KEY = secrets.SUPABASE_KEY