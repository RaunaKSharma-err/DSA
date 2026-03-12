import java.util.Random;

public class HillClimbing {

    // Objective function (e.g., a quadratic function with a peak)
    public static float objectiveFunction(float x) {
        return -(x * x) + 10 * x + 5; // f(x) = -x^2 + 10x + 5
    }

    // Hill Climbing Algorithm
    public static float[] hillClimbing(float start, float stepSize, int maxIterations) {
        float current = start; // Start at the initial solution
        float currentValue = objectiveFunction(current);

        System.out.printf("Starting Hill Climbing at x = %.2f, value = %.2f%n", current, currentValue);

        for (int iteration = 0; iteration < maxIterations; iteration++) {
            // Generate neighbors
            float leftNeighbor = current - stepSize;
            float rightNeighbor = current + stepSize;

            // Evaluate neighbors
            float leftValue = objectiveFunction(leftNeighbor);
            float rightValue = objectiveFunction(rightNeighbor);

            // Choose the best neighbor
            if (leftValue > currentValue && leftValue >= rightValue) {
                current = leftNeighbor;
                currentValue = leftValue;
            }

            else if (rightValue > currentValue && rightValue >= leftValue) {
                current = rightNeighbor;
                currentValue = rightValue;
            }

            else {
                // No better neighbor found, stop at local maximum
                System.out.printf("Local maximum reached at x = %.2f, value = %.2f%n", current, currentValue);
                return new float[] { current, currentValue };
            }

            // Print the current step
            System.out.printf("Step %d: x = %.2f, value = %.2f%n", iteration + 1, current, currentValue);
        }

        System.out.printf("Maximum iterations reached. Final point: x = %.2f, value = %.2f%n", current, currentValue);
        return new float[] { current, currentValue };
    }

    public static void main(String[] args)

    {
        Random random = new Random();

        // Example usage
        float startPoint = -10 + (20 * random.nextFloat()); // Random starting point in the
        // range [-10, 10]
        // This shifts the range of random values to be between -10 and 10 (inclusive of
        // 10 but exclusive of 10).

        float stepSize = 0.5f; // Step size for moving neighbors
        int maxIterations = 100; // Maximum number of iterations

        float[] result = hillClimbing(startPoint, stepSize, maxIterations);
        System.out.printf("Final Solution: x = %.2f, value = %.2f%n", result[0], result[1]);
    }
}