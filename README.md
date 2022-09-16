# SD-Launcher

This is a python script that starts Automatic1111's Stable-Diffusion webui.py with profiles you can edit in one convenient file. Kind of.
This is a bit of re-inventing the wheel, as you can already do essentially what this script is attempting to do by copying and customizing the webui-user.bat file. However, I found it a bit annoying having 5 different webui-user.bat files lying around and customizing / syncing setting across them was kind of annoying.

This thing is basically built for a tiny target audience: me. But I hope that someone else will find this useful.  

## So how do I use this?

- Copy `sd-launcher.py` and `config-example.yaml` into the root folder of your Automatic1111 Webui install
- Copy and/or rename `config-example.yaml` to `config-example.yaml`. Or don't. I'm not your boss. But the script will copy/rename it for you anyway.
- Customize settings to your heart's content. I have included a few settings in the default template that I found most useful to have for different profiles. You *should* be able to add any command-line argument that is included in the `/modules/shared.py` file.
- One thing to note:
  - Arguments that require a value, such as `--ckpt` should be a top-level key : value pair in the config.
  - Arguments that do not, such as `--medvram`, *need* to go under `extra-parameters`.
  - Basically, try to stick to the way it's laid out in the `config-example.yaml`

For example, here's how I run my waifu model:

```
waifu:
  ckpt: custom/waifu.ckpt
  port: 7861
  ui-config:
  ui-settings: custom/waifu-settings.json
  extra-params:
    - --opt-split-attention
```

## Tips

If you want to create profiles here's a few tips:

- config.json:
  - contains all of the settings from your "Settings" Tab.
  - You can make a copy for each model you are playing with and customizing the output directories
- ui-config.json:
  - contains the min, max, and default values for all of the sliders.
  - This is useful in case you find yourself using very different defaults in terms of steps, cfg scale, or sampler depending on wether you are generating Greg Rutkowski masterpiece portraits of anime waifus. But who am I kidding, Greg can do both.
- styles-file:
  - is the .csv file that you can save to and load prompts from. It might be useful to keep seperate copies depending on which model you are working on.
- It's okay to share. You can make use of the same config, settings or styles file in multiple profiles
- You don't need to store all of this stuff in your Stable-Diffusion root folder. I created a /customs folder and put all of my personal config files and extra models in there because I got kind of annoyed at the sheer number of duplicate files I had.

---
PS: this code probably sucks hard, but it works. I guess that's something.
