import streamlit as st
import random

class Player:
    def __init__(self, first_name, last_name, age, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position
        self.stats = self.generate_random_stats(position)

    def generate_random_stats(self, position):
        stats = {}
        if position == "Forward":
            stats["Goals Scored"] = random.randint(5, 20)
            stats["Assists"] = random.randint(2, 15)
        elif position == "Midfielder":
            stats["Goals Scored"] = random.randint(3, 10)
            stats["Assists"] = random.randint(5, 20)
        elif position == "Defender":
            stats["Clean Sheets"] = random.randint(2, 10)
            stats["Tackles"] = random.randint(10, 30)
        elif position == "Goalkeeper":
            stats["Clean Sheets"] = random.randint(5, 15)
            stats["Saves"] = random.randint(20, 60)
        return stats

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

def generate_person_name(region):
    african_first_names = ["Lekan", "Nia", "Chidi", "Fatima", "Mandla", "Zahara", "Kwame", "Amara", "Ifunanya", "Obi", "Ali", "Zainab"]
    european_first_names = ["Sophia", "Liam", "Emma", "Oliver", "Isabella", "Noah", "Amelia", "Ethan", "Ava", "Mia", "James", "Maria"]
    asian_first_names = ["Aarav", "Aisha", "Ji-hoon", "Mei", "Akio", "Anushka", "Hiroshi", "Zara", "Rohan", "Sakura", "Surya", "Lalita"]
    middle_eastern_first_names = ["Yusuf", "Layla", "Khaled", "Leila", "Amin", "Nour", "Zayd", "Aisha", "Amir", "Samira", "Mustafa", "Nadia"]
    
    first_name_list = []
    if region == "African":
        first_name_list = african_first_names
    elif region == "European":
        first_name_list = european_first_names
    elif region == "Asian":
        first_name_list = asian_first_names
    else:
        first_name_list = middle_eastern_first_names
    
    first_name = random.choice(first_name_list)
    return first_name

def generate_player():
    age = random.randint(18, 40)
    positions = ["Forward", "Midfielder", "Defender", "Goalkeeper"]
    position = random.choice(positions)
    return Player(generate_person_name(position), generate_person_name(""), age, position)

def generate_team_squad():
    squad = [generate_player() for _ in range(11)]
    return squad

def main():
    st.title("Soccer Team and Squad Generator App")
    
    team_name = st.session_state.get('team_name', generate_team_name())
    team_manager = st.session_state.get('team_manager', generate_person_name("European"))
    team_owner = st.session_state.get('team_owner', generate_person_name("European"))
    team_squad = st.session_state.get('team_squad', generate_team_squad())
    
    st.write("### Current Soccer Team:")
    st.write(f"Team Name: {team_name}")
    st.write(f"Manager: {team_manager}")
    st.write(f"Owner: {team_owner}")
    
    selected_player = st.selectbox("Select a Player:", [f"{player.first_name} {player.last_name}" for player in team_squad])
    selected_player = selected_player.split()
    selected_player_first_name = selected_player[0]
    selected_player_last_name = selected_player[1]
    
    st.write("Selected Player:")
    for player in team_squad:
        if player.first_name == selected_player_first_name and player.last_name == selected_player_last_name:
            st.write(f"Name: {player.first_name} {player.last_name}")
            st.write(f"Age: {player.age}")
            st.write(f"Position: {player.position}")
            st.write("Statistics:")
            for stat_name, stat_value in player.stats.items():
                st.write(f"{stat_name}: {stat_value}")
            
    st.write("Team Squad:")
    for i, player in enumerate(team_squad, start=1):
        st.write(f"{i}. {player.first_name} {player.last_name} (Age: {player.age}, Position: {player.position})")
    
    if st.button("Generate New Team and Squad"):
        new_team_name = generate_team_name()
        new_team_manager = generate_person_name("European")
        new_team_owner = generate_person_name("European")
        new_team_squad = generate_team_squad()
        st.session_state.team_name = new_team_name
        st.session_state.team_manager = new_team_manager
        st.session_state.team_owner = new_team_owner
        st.session_state.team_squad = new_team_squad

if __name__ == "__main__":
    main()