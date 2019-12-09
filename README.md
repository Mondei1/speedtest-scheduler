# Speedtest-Scheduler
This is just a very small Python-script to measure your bandwidth. All it does is executing the [Speedtest CLI](https://www.speedtest.net/apps/cli) and just appends the start and stop date since the offical speedtest CLI doesn't do that.

Feel free to modify the script as you wish.

## Installing
First make sure you have Python >=3.5 installed.
1. Clone this repository or download it [here](https://github.com/Mondei1/speedtest-scheduler/archive/master.zip)
2. Download the Speedtest CLI tool [here](https://www.speedtest.net/apps/cli) and choose your OS and architecture and save it to the folder where the `main.py` is located
3. Setup a cron job, so that this script get's executed regularly

    Here is one example for what you can write in to your `/etc/crontab`: 
    ``` sh
    # This will execute the speedtest script every 30 minutes
    */30 * * * * root python3 /location/to/script/folder/main.py >> /location/to/script/folder/stats.csv
    ```
    You can also put that into a users cron file but then make sure you remove `root` from the example above.

    **For windows** you can use the [Task Scheduler](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10).
4. Now let cron does its job and you'll see that values appear in that `stats.csv` file

If you have any issues on executing this script feel free to open a issue or write me an email (look at my profile).

## Import
You can use [LibreOffice Calc](https://www.libreoffice.org/download/download/) for example. Just copy the entire file into your clipboard and then paste it into LibreOffice Calc. It will automatically detect it as .csv file and will convert it into its own format. And then you can 