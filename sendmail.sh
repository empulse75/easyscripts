#!/bin/bash
recipient='example@example.com'
subject='put in your mail subject here'
mailcontent='your mail content goes here'
echo $mailcontent | neomutt -s $subject $recipient