#Import the module
Import-Module RabbitMQTools -force


$credRabbit = Get-Credential

Get-RabbitMQOverview -Credentials $credRabbit

$ExchangeName = "GuestExchange"
$QueueName = 'GuestQueue'


Add-RabbitMQExchange -Name $ExchangeName -Type fanout -Durable -VirtualHost /

Get-RabbitMQExchange -Name GuestExchange -ComputerName 'localhost'

Add-RabbitMQQueue $QueueName -VirtualHost /

Get-RabbitMQQueue -Name hello

Add-RabbitMQQueueBinding '/' $ExchangeName $QueueName 'GuestExchange-GuestQueue' 

$Incoming = Get-RabbitMQMessage -VirtualHost / -Name $QueueName -Remove

$IncomingData = $Incoming.payload
$IncomingJson = ConvertFrom-Json -InputObject $IncomingData
foreach ($name in $IncomingJson){
    Write-Host $name.source.name
    Write-Host $name.source.path_collection.entries.name
}




