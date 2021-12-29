<?php
function callAPI($url){
   $curl = curl_init();
   curl_setopt($curl, CURLOPT_URL, $url);
   curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
   $result = curl_exec($curl);
   curl_close($curl);
   return json_decode($result);
}
function buildArray($firstLetter, $job, $temp){
   return array('firstLetter' => $firstLetter, 'state' => $job->state, 'printTimeLeft' => $job->progress->printTimeLeft, 'printTime' => $job->progress->printTime, 'nozzleTemp' => $temp->temperature->tool0->actual, 'nozzleTempTarget' => $temp->temperature->tool0->target, 'bedTemp' => $temp->temperature->bed->actual, 'bedTempTarget' => $temp->temperature->bed->target);
}


$ret['h'] = buildArray('h', $h_job, $h_temp);

$ret['k'] = buildArray('k', $k_job, $k_temp);

$ret['p'] = buildArray('p', $p_job, $p_temp);

echo json_encode($ret);
