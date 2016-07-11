<?php

require_once __DIR__.'/vendor/autoload.php';

use Cocur\Slugify\Bridge\Twig\SlugifyExtension;
use Cocur\Slugify\Slugify;

$dump = file_get_contents("swagger.json");
$spec = json_decode($dump, true); // array (because twig requires array)

$global_spec_parameters = $spec['parameters'];
$global_spec_definitions = $spec['definitions'];

function ref_parser($spec){
  global $global_spec_parameters;
  global $global_spec_definitions;

  foreach($spec as $some_key=>$some_val){
    if($some_key === '$ref'){
      // replace with ref
      $ref = explode("/", $some_val, 3);
      $referred_from = $ref[1];
      $referred_to = $ref[2];
      if($referred_from == 'definitions'){
        return $global_spec_definitions[$referred_to];
      }elseif($referred_from == 'parameters'){
        return $global_spec_parameters[$referred_to];
      }
    }elseif(is_array($some_val)){
      $spec[$some_key] = ref_parser($some_val);
    }
  }
  return $spec;
}
$spec = ref_parser($spec);

$loader = new Twig_Loader_Filesystem(__DIR__);
$twig = new Twig_Environment($loader);
$twig->addExtension(new SlugifyExtension(Slugify::create()));

echo $twig->render('generator.template.html', $spec);
?>

<pre style="display:none">
<?php print_r($spec); ?>
</pre>
