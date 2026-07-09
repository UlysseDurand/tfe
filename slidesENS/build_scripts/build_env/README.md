# Manual steps before build (`manual_build`)

- Give `prompt` to a LLM with Stage/Livrables/(PR+Issues) copied as Markdown,
and paste the response to assets/infos/accomplished.yml

```
can you make a yml out of this

I want like 
PR: 
    - url: 
      description:
    - ...
    ...

issues: 
    - url:
      description:
    - ...
    ...

[Paste the markdown]
```

- Give the calendar URL

In a `.env` file, write
```
CALENDAR_URL=[insert calendar URL .ics]
```
The calendar URL can be found in the settings of google calendar