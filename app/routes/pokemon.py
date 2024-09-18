from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.pokeapi import get_pokemon
from app.models import User

bp = Blueprint('pokemon', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/pokemon/search', methods=['POST'])
def search_pokemon():
    pokemon_name = request.form.get('pokemon_name')
    return redirect(url_for('pokemon.show_pokemon', name=pokemon_name))

@bp.route('/pokemon/<name>')
def show_pokemon(name):
    pokemon = get_pokemon(name.lower())
    if pokemon:
        return render_template('pokemon.html', pokemon=pokemon)
    flash('Pokemon not found', 'danger')
    return redirect(url_for('pokemon.index'))
