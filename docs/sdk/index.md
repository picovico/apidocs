Picovico provides `SDK` for ease of use with the API. SDK are available in [github](https://github.com/picovico).

###PHP-SDK

Available [here](https://github.com/picovico/php-sdk)

__Usage__

    <?php
        require __DIR__."/Lib3.php";
        use \Picovico\Lib3 as Picovico;
        # initialize and authenticate
        $app_id = getenv("PV_2017_APP_ID");
        $app_secret = getenv("PV_2017_APP_SECRET");
        $device_id = getenv("PV_2017_DEVICE_ID");
        $pv = new Picovico($app_id, $app_secret, $device_id);
        $pv->authenticate();
        # build the video JSON
        $payload = [
            "style" => "vanilla_frameless",
            "quality" => 360,
            "name" => "Sample Video",
            "aspect_ratio" => "16:9",
            "assets" => [
                [
                    "music" => [
                        "id" => "aud_6j44J9zjbSQe54ZTTSqUj2"
                        # "url" => ".... some url ..."
                    ],
                    "frames" => [
                        $pv->text_slide("You are", "my love"),
                        $pv->text_slide("You are", "CSS to my HTML"),
                        $pv->image_slide("https://images.unsplash.com/photo-1481326086332-e77dd61a4ea1"),
                        $pv->text_slide("You", "make me complete")
                    ]
                ]
            ]
        ];
        list($status, $code, $response) = $pv->authenticated_api("POST", "me/videos", $payload, ["Content-Type"=>"application/json"]);
        if($status){
            $video_id = $response['data'][0]['id'];
            # preview
            // $pv->authenticated_api("PUT", "me/videos/{$video_id}", ["preview"=>1]);
            # render
            $responses = $pv->authenticated_api("PUT", "me/videos/{$video_id}");
            print_r($responses);
        }else{
            print_r($response);
        }

   


###Python SDK

Available [here](https://github.com/picovico/python-sdk)


__Usage__


    from __future__ import print_function
    import json

    from picovico.exceptions import PicovicoError
    from picovico import PicovicoAPI2 as PicovicoAPI

    APP_ID = ''
    APP_SECRET = ''
    DEVICE_ID = ''
    
    picovico = PicovicoAPI(APP_ID, APP_SECRET, DEVICE_ID)
    picovico.authenticate()
    payload = {
        "style" : "vanilla_frameless",
        "quality" : 360,
        "name" : "Sample Video",
        "aspect_ratio" : "16:9",
        "assets" : [{
                "music" : {
                    "id" : "aud_6j44J9zjbSQe54ZTTSqUj2"
                }
                ,
                "frames" : {
                    pv.text_slide(title="You are", body="my love"),
                    pv.text_slide(title="You are", body="CSS to my HTML"),
                    pv.image_slide(image_url="https://images.unsplash.com/photo-1481326086332-e77dd61a4ea1"),
                    pv.text_slide(title="You", body="make me complete")
                }
            }
        ]
    }
    try:
        res = pv.authenticated_api(method='post', url='me/videos', json.dumps(payload), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
    except PicovicoError as e:
        print(str(e))
    else:
        print(res)

