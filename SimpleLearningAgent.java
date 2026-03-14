import java.util.*;

public class SimpleLearningAgent { 
	private static final int GRID_SIZE = 3;   // Grid size (3x3) 
	private static final int GOAL_X = 2;      
	private static final int GOAL_Y = 2; 
	private int agentX = 0;                  
	private int agentY = 0; 
	private int stepCount = 0;               
	
	
	public SimpleLearningAgent() 
	
	{ 
	// Initialize agent at (0,0) 
	this.agentX = 0; 
	this.agentY = 0; 
	this.stepCount = 0; 
	// Goal position (2, 2) 
	// Agent's current position 
	// Counter for steps taken 
	} 
	// Reset the agent's position 
	
	
	public void reset()
	
	{ 
	this.agentX = 0; 
	this.agentY = 0; 
	this.stepCount = 0; 
	} 
	// Method to move the agent (choose an action) 
	
	public void move(String action) 
	
	{ 
	
		switch (action) 
	                  { 
	
	case "up": 
	if (agentX > 0) 
		agentX--; 
	break; 
	
	case "down": 
	if (agentX < GRID_SIZE - 1) 
		agentX++; 
	break; 
	
	case "left": 
	if (agentY > 0) 
		agentY--; 
	break; 
	
	case "right": 
	
		if (agentY < GRID_SIZE - 1) agentY++; 
	break; 
	} 
	} 
	// Method to get the reward based on agent's position 
	public int getReward() { 
	if (agentX == GOAL_X && agentY == GOAL_Y) { 
	return 1;  // Reward for reaching the goal 
	} 
	return -1;  // Penalty for each move 
	} 
	// Method to print the current grid position of the agent 
	public void printAgentPosition() { 
	System.out.println("Agent is at (" + agentX + ", " + agentY 
	+ ")"); 
	} 
	// Method to choose a random action for the agent 
	public String chooseRandomAction() 
	{ 
	List<String> actions = Arrays.asList("up", "down", "left", "right"); 
	return actions.get(new Random().nextInt(actions.size()));  
	// Random action 
	} 
	// Method for the agent to learn by taking actions 
	public void learn(int episodes)
	{ 
	for (int i = 0; i < episodes; i++) { 
	reset();  // Reset the agent for each episode 
	boolean done = false; 
	while (!done) 
	{ 
	// Agent chooses an action randomly 
	String action = chooseRandomAction(); 
	move(action);  // Move the agent 
	stepCount++; 
	// Get the reward based on the new position 
	int reward = getReward(); 
	printAgentPosition();  // Print the current position 
	// If the agent reached the goal, stop the episode 
	if (reward == 1) { 
	done = true; 
	System.out.println("Goal reached in " + stepCount 
	+ " steps."); 
	} else { 
	System.out.println("Reward: " + reward); 
	} 
	} 
	} 
	} 
	public static void main(String[] args) { 
	SimpleLearningAgent agent = new 
	SimpleLearningAgent(); 
	System.out.println("\n\n\tStarting learning process..."); 
	agent.learn(10);  // Run 10 episodes of learning 
	}}