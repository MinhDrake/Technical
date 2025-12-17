
public class RotateImage {
  public void rotate(int[][] matrix) {
    int n = matrix.length;
    var temp = 0;

    // transpose
    for (int i = 0; i < n; i++) {
      for (int j = i; j < n; j++) {
        if (i != j) {
          temp = matrix[i][j];
          matrix[i][j] = matrix[j][i];
          matrix[j][i] = temp;
        }
      }
    }

    // reverse row
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n / 2; j++) {
        temp = matrix[i][j];
        matrix[i][j] = matrix[i][n - 1 - j];
        matrix[i][n - 1 - j] = temp;
      }
    }
  }

  public static void main(String[] args) {
    RotateImage sol = new RotateImage();
    int[][] matrix = {
        { 1, 2, 3 },
        { 4, 5, 6 },
        { 7, 8, 9 }
    };
    sol.rotate(matrix);
    for (int[] matrix1 : matrix) {
      for (int j = 0; j < matrix[0].length; j++) {
        System.out.print(matrix1[j] + " ");
      }
      System.out.println();
    }
  }
}
