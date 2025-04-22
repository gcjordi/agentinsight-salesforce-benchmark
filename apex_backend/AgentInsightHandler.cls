// Apex logic placeholder for AgentInsight actions
public class AgentInsightHandler {
    public static Integer evaluateResponse(String inputText) {
        // Simulate a score from 0 to 2
        return Math.mod(inputText.length(), 3);
    }
}
