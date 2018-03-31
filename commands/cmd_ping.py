import time


async def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n*Attached arguments: %s*" % args.__str__()[1:-1].replace("'", "")
    t = time.process_time()
    await client.send_message(message.channel, "Pong!" + args_out)
    elapsed_time = time.process_time() - t

    await client.send_message(message.channel, "~ %sms" % elapsed_time)