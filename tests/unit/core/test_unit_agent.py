from core.agent import Agent


def test_agent_calls_a_server_synchronously():
    agent = Agent()
    result = agent.process("1", "https://www.example.com")
    assert result[1] == 200
