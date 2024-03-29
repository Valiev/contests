import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
  public static void main(String[] args) {
    int counter = 0;
    String champion = "";
    while (! StdIn.isEmpty()) {
      String value = StdIn.readString();
      counter += 1;
      if (StdRandom.bernoulli(1.0 / counter)) {
        champion = value;
      }
    }
    StdOut.println(champion);
  }
}
