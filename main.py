from my_agent.agent import extract_city, get_city_time
def run_agent():
    print("My AI Time Agent is running")

    while True:
        user_input = input("\nUser: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye ")
            break

        city = extract_city(user_input)

        if not city:
            print("Agent: Please ask like 'tell me time of pune'")
            continue

        time_now = get_city_time(city)

        if not time_now:
            print(f"Agent: Sorry, I don't know the time for {city}.")
        else:
            print(f"Agent: Current time in {city.title()} is {time_now}")


if __name__ == "__main__":
    run_agent()
