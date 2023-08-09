import streamlit as st
import random

class Player:
    def __init__(self, first_name, last_name, age, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position

class Team:
    def __init__(self, name, manager, owner, squad):
        self.name = name
        self.manager = manager
        self.owner = owner
        self.squad = squad

def generate_team_name():
    adjectives = ["Fierce", "Mighty", "Swift", "Bold", "Dynamic", "Radiant", "Thundering", "Energetic", "Elegant"]
    nouns = ["Lions", "Dragons", "Phoenixes", "Titans", "Gladiators", "Warriors", "Cobras", "Hurricanes", "Raiders"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

def generate_person_name():
    first_names = ["John", "Emily", "Michael", "Emma", "David", "Sarah", "Daniel", "Olivia", "Robert", "Sophia"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_player():
    age = random.randint(18, 40)
    positions = ["Forward", "Midfielder", "Defender", "Goalkeeper"]
    return Player(generate_person_name(), generate_person_name(), age, random.choice(positions))

def generate_team_squad():
    squad = [generate_player() for _ in range(11)]
    return squad

def main():
    st.title("Soccer Team and Squad Generator App")
    
    team_name = st.session_state.get('team_name', generate_team_name())
    team_manager = st.session_state.get('team_manager', generate_person_name())
    team_owner = st.session_state.get('team_owner', generate_person_name())
    team_squad = st.session_state.get('team_squad', generate_team_squad())
    
    st.write("### Current Soccer Team:")
    st.write(f"Team Name: {team_name}")
    st.write(f"Manager: {team_manager}")
    st.write(f"Owner: {team_owner}")
    st.write("Team Squad:")
    for i, player in enumerate(team_squad, start=1):
        st.write(f"{i}. {player.first_name} {player.last_name} (Age: {player.age}, Position: {player.position})")
    
    if st.button("Generate New Team and Squad"):
        new_team_name = generate_team_name()
        new_team_manager = generate_person_name()
        new_team_owner = generate_person_name()
        new_team_squad = generate_team_squad()
        st.session_state.team_name = new_team_name
        st.session_state.team_manager = new_team_manager
        st.session_state.team_owner = new_team_owner
        st.session_state.team_squad = new_team_squad
        st.write("### New Soccer Team:")
        st.write(f"Team Name: {new_team_name}")
        st.write(f"Manager: {new_team_manager}")
        st.write(f"Owner: {new_team_owner}")
        st.write("Team Squad:")
        for i, player in enumerate(new_team_squad, start=1):
            st.write(f"{i}. {player.first_name} {player.last_name} (Age: {player.age}, Position: {player.position})")

if __name__ == "__main__":
    main()