<h2>Zoo Database</h2>

<p>Selecting everything from animals where id is: </p>

<?php
  try {
    $records = [];
    if (isset($_POST['id'])) {
      $id = $_POST['id'];

      $pdo = new PDO(
        'mysql:host=mysql;dbname=sample',
        'devuser',
        'devpass'
      );
      $prepare = $pdo->prepare('SELECT * FROM animals WHERE id = ' . $id . ';');
      $prepare->execute();
      $records = $prepare->fetchAll(PDO::FETCH_ASSOC);

      foreach ($records as $record) {
        echo "name = " . $record['name'].PHP_EOL . "<br>";
      }
    }
  } catch (PDOException $e) {
    echo "Error: ";
    echo $e->getMessage();
  }
?>

<form method="post">
  <input type="id" name="id" value="1">
  <input type="submit" value="submit">
</form>
