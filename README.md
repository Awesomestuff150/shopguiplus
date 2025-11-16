Adding new shops
First, head to the /plugins/ShopGUIPlus/shops/ directory. You can find all default and previously added shops in there . Each file is responsible for a single shop.

This is an example of armor.yml file:

armor:
  name: "&4&lArmor (page %page%)"
  fillItem:
    material: STAINED_GLASS_PANE
    damage: 15
    name: " "
  items:
    1:
      type: item
      item:
        material: LEATHER_HELMET
        quantity: 1
      buyPrice: 40
      sellPrice: 8
      slot: 10
    2:
      type: item
      item:
        material: GOLD_HELMET
        quantity: 1
      buyPrice: 160
      sellPrice: 32
      slot: 11
As you can see, first of all you have to define the id of the shop (has to be unique, you will refer to it later in the main config). This name must also match the file's name (armor.yml and armor in here):

armor:
Now you have to set the displayed name of the shop which will be visible in the GUI:

armor:
  name: "&4&lArmor (page %page%)"
You can also set fill item for the entire shop, a gray glass pane in this case:

armor:
  name: "&4&lArmor (page %page%)"
  fillItem:
    material: STAINED_GLASS_PANE
    damage: 15
    name: " "
Then you can proceed to adding new items. You need items section with the same indentation as previously added name.

armor:
  name: "&4&lArmor (page %page%)"
  fillItem:
    material: STAINED_GLASS_PANE
    damage: 15
    name: " "
  items:
Now, to add an item you have to create another section with higher indentation. Name it whatever you want (only alphanumeric characters), just remember the names have to be unique for each item. Then you have to add the '''type''' of the shop item. Valid types are item, permission, enchantment, command or dummy.

armor:
  name: "&4&lArmor (page %page%)"
  fillItem:
    material: STAINED_GLASS_PANE
    damage: 15
    name: " "
  items:
    1:
      type: item
Next you have to add the item meta like material, quantity etc. For more information on item meta please refer to the Item meta page.

armor:
  name: "&4&lArmor (page %page%)"
  fillItem:
    material: STAINED_GLASS_PANE
    damage: 15
    name: " "
  items:
    1:
      type: item
      item:
        material: LEATHER_HELMET
Finally, you can proceed to basic information like buy/sell price and GUI slot number. Setting buyPrice or sellPrice to -1 will result in unbuyable/unsellable item. Remember that slot numbers go from 0 to 53.

armor:
  name: "&4&lArmor (page %page%)"
  fillItem:
    material: STAINED_GLASS_PANE
    damage: 15
    name: " "
  items:
    1:
      type: item
      item:
        material: LEATHER_HELMET
        quantity: 1
      buyPrice: 40
      sellPrice: 8
      slot: 10
Optionally, you can customise the number of rows in the shop gui by setting a size property.

Accepted values: 9, 18, 27, 36, 45, 54

armor:
  name: "&4&lArmor (page %page%)"
  size: 45
  fillItem:
    material: STAINED_GLASS_PANE
    damage: 15
    name: " "
  items:
    1:
      type: item
      item:
        material: LEATHER_HELMET
        quantity: 1
      buyPrice: 40
      sellPrice: 8
      slot: 10
Now you have to add the shop to the main menu, otherwise players couldn't access it. Open the config.yml and proceed to shopMenuItems section. You can see there all previously added shops.

shopMenuItems:
  # Has to be unique, value doesn't matter
  1:
    item:
      # The same rules apply for material, amount, damage and lore as for goBackButton
      material: DIAMOND_CHESTPLATE
      quantity: 1
      name: "&4&lArmor"
    # Shop ID from shop yaml
    shop: "armor"
    # Slot in shops menu, counting from 0 to 53
    slot: 15
We're done with our first shop. If you have any questions or errors please contact us at our Discord server.

Adding items to shops
Now we want to add some more items to previously created shop. Let's start from what we've got at the end of the previous tutorial section.

food:
  #Shop inventory name
  name: "&5Food Shop"
  items:
    #Has to be unique for each of items, value doesn't matter
    1:
      type: item
      item:
        #Material name, full list can be found here: https://docs.brcdev.net/#/materials
        material: BREAD
        #(optional) Quantity of the item
        quantity: 32
        #(optional) Data value, for example 1 for WOOD:1 means spruce wood planks
        damage: 0
        #(optional) Custom name
        name: "&aYummy bread"
        #(optional) Lore, can contain multiple lines
        lore:
          - "&3<3"
      #Buy price, lower than 0 means you can't buy it, 0 mean free, higher than 0 is regular value
      buyPrice: -1
      #Same as above but sell price
      sellPrice: 25
      #Slot in shop's inventory, counting from 0 to 53
      slot: 0
In order to add more items, you have to add more sections as section named '''1''' in this case. Remember all sections have to have unique names, so you can just call them 1, 2, 3, 4... etc.

food:
  #Shop inventory name
  name: "&5Food Shop"
  items:
    #Has to be unique for each of items, value doesn't matter
    1:
      type: item
      item:
        #Material name, full list can be found here: https://docs.brcdev.net/#/materials
        material: BREAD
        #(optional) Quantity of the item
        quantity: 32
        #(optional) Data value, for example 1 for WOOD:1 means spruce wood planks
        damage: 0
        #(optional) Custom name
        name: "&aYummy bread"
        #(optional) Lore, can contain multiple lines
        lore:
          - "&3<3"
      #Buy price, lower than 0 means you can't buy it, 0 mean free, higher than 0 is regular value
      buyPrice: -1
      #Same as above but sell price
      sellPrice: 25
      #Slot in shop's inventory, counting from 0 to 53
      slot: 0
    2:
Then just repeat steps from the previous tutorial section, add the type, item, prices and slot number:

food:
  #Shop inventory name
  name: "&5Food Shop"
  items:
    #Has to be unique for each of items, value doesn't matter
    1:
      type: item
      item:
        #Material name, full list can be found here: https://docs.brcdev.net/#/materials
        material: BREAD
        #(optional) Quantity of the item
        quantity: 32
        #(optional) Data value, for example 1 for WOOD:1 means spruce wood planks
        damage: 0
        #(optional) Custom name
        name: "&aYummy bread"
        #(optional) Lore, can contain multiple lines
        lore:
          - "&3<3"
      #Buy price, lower than 0 means you can't buy it, 0 mean free, higher than 0 is regular value
      buyPrice: -1
      #Same as above but sell price
      sellPrice: 25
      #Slot in shop's inventory, counting from 0 to 53
      slot: 0
    2:
      type: item
      item:
        material: COOKED_RABBIT
        quantity: 10
        damage: 0
      buyPrice: 75.5
      sellPrice: -1
      slot: 1
We're done with the second item. You can add up to 54 items to each shop this way.

Items
Pickaxe with custom name & Efficiency I

      1:
        type: item
        item:
          material: STONE_PICKAXE
          quantity: 1
          name: "&8Crappy Pickaxe"
          enchantments:
            - EFFICIENCY:1
        buyPrice: 50
        sellPrice: 25
        slot: 0
Firework

      1:
        type: item
        item:
          material: FIREWORK
          quantity: 32
          damage: 0
          fireworkPower: 2
          fireworkEffects:
            1:
              type: BALL_LARGE
              colors:
               - YELLOW
               - ORANGE
            2:
              type: CREEPER
              colors:
               - YELLOW
               - ORANGE
        buyPrice: 10
        sellPrice: -1
        slot: 0
Custom items
Brewery
Brewery wine potion with quality 10

      1:
        type: item
        item:
          brewery:
            recipe: "wine"
            quality: 10
        buyPrice: 50
        sellPrice: 25
        slot: 0
CrackShot
CrackShot gun with ID AK-47

      1:
        type: item
        item:
          crackShot: "AK-47"
        buyPrice: 50
        sellPrice: 25
        slot: 0
CraftEngine
CraftEngine item with namespace customcrops and item ID apple

      1:
        type: item
        item:
          craftEngine: "customcrops:apple"
        buyPrice: 50
        sellPrice: 25
        slot: 0
Custom Items
Custom Items item with ID item1

      1:
        type: item
        item:
          customItems: "item1"
        buyPrice: 50
        sellPrice: 25
        slot: 0
Executable Blocks
Item from Executable Blocks with ID teleporter

      1:
        type: item
        item:
          executableBlocks: "teleporter"
        buyPrice: 50
        sellPrice: 25
        slot: 0
Executable Items
Item from Executable Items with ID heal

      1:
        type: item
        item:
          executableItems: "heal"
        buyPrice: 50
        sellPrice: 25
        slot: 0
HeadDatabase
Head from HeadDatabase with ID 1734

      1:
        type: item
        item:
          headDatabase: 1734
        buyPrice: 50
        sellPrice: 25
        slot: 0
ItemsAdder
Note: If you're having issues with ItemsAdder items not loading in ShopGUIPlus, try re-generating your ItemsAdder Storage folder (/plugins/ItemsAdder/storage) by deleting it and restarting your server.

Item from ItemsAdder with ID ruby_sword

      1:
        type: item
        item:
          itemsAdder: "ruby_sword"
        buyPrice: 50
        sellPrice: 25
        slot: 0
You can also use the Custom Model Data from ItemsAdder items to display them in the shop. Note that it is only recommended for displaying and not purchasable/sellable items.

Run /iatag while holding any ItemsAdder item to get the Custom Model Data Value:

image

      1:
        type: dummy
        item:
          item: paper
          name: "Example Item with ItemsAdder Texture"
          model: 10002
        slot: 0
Click here for more information on Custom Model Data in ShopGUIPlus.

MMOItems
Item from MMOItems with type armor and id MYTHRIL_CHAINMAIL

      1:
        type: item
        item:
          mmoItems:
            type: ARMOR
            id: MYTHRIL_CHAINMAIL
        buyPrice: 50
        sellPrice: 25
        slot: 0
MythicMobs
Item from MythicMobs with ID PIG_BONE

      1:
        type: item
        item:
          mythicMobs: 
            item: "PIG_BONE"
        buyPrice: 50
        sellPrice: 25
        slot: 0
Spawner Item from MythicMobs with Mob Type PENGUIN

      1:
        type: item
        item:
          mythicMobs: 
            spawner: "PENGUIN"
        buyPrice: 50
        sellPrice: 25
        slot: 0
Spawn Egg Item from MythicMobs with Mob Type FIRE_DRAGON

      1:
        type: item
        item:
          mythicMobs: 
            egg: "FIRE_DRAGON"
        buyPrice: 50
        sellPrice: 25
        slot: 0
Nexo
Nexo item with ID mithril_helmet

      1:
        type: item
        item:
          nexo: "mithril_helmet"
        buyPrice: 50
        sellPrice: 25
        slot: 0
Oraxen
Oraxen item with ID obsidian_pickaxe

      1:
        type: item
        item:
          oraxen: "obsidian_pickaxe"
        buyPrice: 50
        sellPrice: 25
        slot: 0
QualityArmory
Item from QualityArmory with ID PISTOL

      1:
        type: item
        item:
          qualityArmory: "PISTOL"
        buyPrice: 50
        sellPrice: 25
        slot: 0
Slimefun
Item from Slimefun with ID GRANDMAS_WALKING_STICK

      1:
        type: item
        item:
          slimefun: "GRANDMAS_WALKING_STICK"
        buyPrice: 50
        sellPrice: 25
        slot: 0
Mob spawners
Note: Remember to use valid material name corresponding to your Minecraft version (SPAWNER or MOB_SPAWNER).

The mob entry has to represent a valid entity name. List of all entity types

Pig spawner with a custom name

      1:
        type: item
        item:
          material: SPAWNER
          mob: PIG
          name: "&dPig spawner"
          quantity: 1
        buyPrice: 10
        sellPrice: -1
        slot: 0
5 blaze spawners

      2:
        type: item
        item:
          material: SPAWNER
          mob: BLAZE
          quantity: 5
        buyPrice: 10
        sellPrice: -1
        slot: 1
Enchantments
Fortune II

      1:
        type: enchantment
        enchantment: FORTUNE
        enchantmentLevel: 2
        item:
          material: DIAMOND_PICKAXE
          quantity: 1
          name: "&8Fortune II"
          enchantments:
            - FORTUNE:2
        buyPrice: 50
        slot: 0
Knockback I

      1:
        type: enchantment
        enchantment: KNOCKBACK
        enchantmentLevel: 1
        item:
          material: DIAMOND_SWORD
          quantity: 1
          name: "&6Knockback I"
        buyPrice: 1000
        slot: 1
Permissions
Single permission essentials.msg valid in all worlds

      1:
        type: permission
        permission: "essentials.msg"
        item:
          material: STONE_PICKAXE
          quantity: 1
          name: "&8/msg permission"
          enchantments:
            - EFFICIENCY:1
            - FORTUNE:2
        buyPrice: 50
        sellPrice: 25
        slot: 0
Multiple permissions essentials.msg and essentials.afk valid in all worlds

      2:
        type: permission
        permissions:
          - "essentials.me"
          - "essentials.afk"
        item:
          material: DIAMOND_PICKAXE
          quantity: 1
          name: "&aPermission to use /me"
        buyPrice: 1000
        sellPrice: 500
        slot: 1
Multiple permissions essentials.balance and essentials.balance.others valid only in specific worlds

      2:
        type: permission
        permissions:
          1:
            permission: "essentials.balance"
            world: "world"
          2:
            permission: "essentials.balance.others"
            world: "world_nether"
        item:
          material: DIAMOND_PICKAXE
          quantity: 1
          name: "&aPermission to use /me"
        buyPrice: 1000
        sellPrice: 500
        slot: 1
Commands
If you are wanting to add a shop item that isn't for purchase but executes a command when clicked, see here

Selling single command: /say Hello [player name]!

      1:
        type: command
        item:
          material: DIAMOND_PICKAXE
          quantity: 1
        commands:
          - "say Hello, %PLAYER%!"
        buyPrice: 100
        slot: 0
Selling multiple commands at once:

/say Good bye [player name]!
/msg [player name] See you later!
      1:
        type: command
        item:
          material: DIAMOND_PICKAXE
          quantity: 1
        commands:
          - "say Good bye, %PLAYER%!"
          - "msg %PLAYER% See you later!"
        buyPrice: 100
        slot: 0
Allowing players to purchase multiple executions (quantity is limited by the value of commandsLimit) of a single command:

      1:
        type: command
        item:
          material: DIAMOND_PICKAXE
          quantity: 1
        commands:
          - "say Sup %PLAYER%"
        commandsLimit: 64
        buyPrice: 100
        slot: 0
Allowing players to purchase single execution (quantity is limited by the value of commandsLimit) of a single command with placeholder %AMOUNT% being replaced with purchased quantity:

      1:
        type: command
        item:
          material: DIAMOND_PICKAXE
          quantity: 1
        commands:
          - "say Sup %PLAYER%, you bought %AMOUNT% commands"
        commandsLimit: 64
        runSingleCommand: true
        buyPrice: 100
        slot: 0
Requiring an empty slots in buyer's inventory (i.e. for commands giving items to the player):

      1:
        type: command
        item:
          material: STICK
          quantity: 1
        commands:
          - "give %PLAYER% stick 1"
        requireInventorySpace: true
        buyPrice: 100
        slot: 0
Shop links
You can directly link shops to each other using link items. All you have to do is specify the other shop ID to be opened.

Example:

    1:
      type: shop_link
      link:
        shop: "blocks"
        page: 2 # <--- Optional, defaults to page 1 if not set.
      item:
        material: STONE
        quantity: 1
        name: "&fBlocks shop"
      slot: 10
Decorations
You can add items to your shops and main menu that are purely cosmetic thus are not purchasable or sellable, we call these dummy items.

Example:

     1:
      type: dummy
      item:
        material: STONE
        quantity: 1
        name: "&fThis is an example of a dummy item"
      slot: 10
Custom / Alternative Buttons
You can add custom / alternative buttons to your shops and main menu by using dummy items with commandsOnClick.

Example with command ran through console (commandsOnClickConsole):

     1:
      type: dummy
      item:
        material: STONE
        quantity: 1
        name: "&fThis is an example of a dummy item with commandsOnClickConsole"
      commandsOnClickConsole:
      - "say Hello %PLAYER%, you clicked a custom / alternative button" # Send a messages in chat
      slot: 10
Example with command ran through the player (commandsOnClick):

     1:
      type: dummy
      item:
        material: STONE
        quantity: 1
        name: "&fThis is an example of a dummy item with commandsOnClick"
      commandsOnClick:
      - "shop block" # Opens the blocks shop
      slot: 10
Adding same item to multiple slots
You can add the same item multiple times to a shop by specifying the slots numbers as a list instead of a single value:

       1:
         type: DUMMY
         item:
           material: STONE
           quantity: 1
         slots:
           - 30
           - 31
           - 32
Amount selection GUI customization
You can change every part of the amount selection GUI in the config. You can change items/slots, hide buttons etc.

All necessary settings are included in the amountSelectionGUI section of config.yml:

amountSelectionGUI:
  #Size of the GUI, valid values are 9, 18, 27, 36, 45 and 54
  size: 54
  #Slot of the item being bought/sold
  itemSlot: 22
  #Buttons
  buttons:
    #"Set to 1" button
    set1:
      item:
        material: RED_STAINED_GLASS_PANE
        quantity: 1
        name: "&c&lSet to 1"
      slot: 18
    #"Remove 10" button
    remove10:
      item:
        material: RED_STAINED_GLASS_PANE
        quantity: 10
        name: "&c&lRemove 10"
      slot: 19
    #"Remove 1" button
    remove1:
      item:
        material: RED_STAINED_GLASS_PANE
        quantity: 1
        name: "&c&lRemove 1"
      slot: 20
    #"Add 1" button
    add1:
      item:
        material: GREEN_STAINED_GLASS_PANE
        quantity: 1
        name: "&a&lAdd 1"
      slot: 24
    #"Add 10" button
    add10:
      item:
        material: GREEN_STAINED_GLASS_PANE
        quantity: 10
        name: "&a&lAdd 10"
      slot: 25
    #"Set to 64" button
    set64:
      item:
        material: GREEN_STAINED_GLASS_PANE
        quantity: 64
        name: "&c&lSet to 64"
      slot: 26
    #"Confirm" button
    confirm:
      item:
        material: GREEN_STAINED_GLASS
        quantity: 1
        name: "&a&lConfirm"   
      slot: 39
    #"Sell all" button
    sellAll:
      item:
        material: GREEN_STAINED_GLASS
        quantity: 1
        name: "&a&lSell all"      
      slot: 40
    #"Cancel" button      
    cancel:
      item:
        material: RED_STAINED_GLASS
        quantity: 1
        name: "&c&lCancel"  
      slot: 41
In order to change the button item you have to edit the appropriate entry.

Setting the slot to -1 will result in the button being hidden.

Changing sizes/buttons of shops
You can change the size of any shop as well as next/previous page/go back button slots.

Just change/add the size entry to any of the shops yaml:

food:
  #Shop inventory name
  name: "&5Food Shop (page %page%)"
  #(Optional) Shop inventory size (valid values are 9, 18, 27, 36, 45 and 54)
  size: 45
Note: Sometimes it might be necessary to adjust the button slots in each shop according to the instructions below, if the target inventory size is too small.

These global settings from config.yml apply to every shop unless you override the item/slot/both for a specific shop:

buttons:
  #"Go back button"
  goBack:
    item:
      #Material name, full list can be found here: https://docs.brcdev.net/#/materials
      material: NETHER_STAR
      #Amount of the item
      amount: 1
      #(optional) Data value, for example 1 for WOOD:1 means spruce wood planks
      damage: 0
      #(optional) Custom name
      name: "&cBack to categories"
      #(optional) Lore, can contain multiple lines
      lore:
        - "&aClick here to return to the main menu"
    #Slot in each shop's GUI
    slot: 49
  #"Previous page" button
  previousPage:
    item:
      material: PAPER
      quantity: 1
      name: "&e&lPrevious page"
    slot: 45
  #"Next page" button
  nextPage:
    item:
      material: PAPER
      quantity: 1
      name: "&e&lNext page"
    slot: 53
You can edit them for any shop using the same entry names/indentation:

food:
  #Shop inventory name
  name: "&5Food Shop (page %page%)"
  #(Optional) Shop inventory size (valid values are 9, 18, 27, 36, 45 and 54)
  size: 45
  #(Optional) Changed button types/slots
  buttons:
    goBack:
      #Slot -1 means it's hidden
      slot: 40
    previousPage:
      #You can change the item as well
      item:
        material: INK_SACK
        quantity: 1
        damage: 15
      slot: 36
    nextPage:
      slot: 44
You can edit only the item or slot or both as well.

Using per item permissions
First, you have to add the enablePerItemPermissions: true entry to your shop in the shop yaml:

mining:
  name: "&2Mining Shop (page %page%)"
  enablePerItemPermissions: true
  items:
    1:
      type: item
      item:
        material: STONE_PICKAXE
        quantity: 1
        name: "&8Crappy Pickaxe"
        enchantments:
          - EFFICIENCY:1
      buyPrice: 50
      sellPrice: 25
      slot: 0
    2:
      type: item
      item:
        material: DIAMOND_PICKAXE
        quantity: 5
      buyPrice: 1000
      sellPrice: 500
      slot: 1
      unstack: true
    3:
      type: item
      item:
        material: IRON_SPADE
        damage: 125
        quantity: 1
        enchantments:
          - EFFICIENCY:1
      buyPrice: 750
      sellPrice: 111.11
      slot: 2
Then you have to give your players appropriate permissions. The format of permissions is shopguiplus.item.<shop id>.<item id>.

The item ID is this number:

    items:
      1:
For instance, permissions for these 3 items in shop above would be shopguiplus.item.mining.1 , shopguiplus.item.mining.2 and shopguiplus.item.mining.3.

You can use shopguiplus.item.<shop id>.* wildcard permission (eg. shopguiplus.item.mining.*) to give access to all items within particular shop.

Setting per-shop economy
In order to use another economy within a single shop, set the economy field in shop's yml to the economy name:

armor:
  name: "&4&lArmor (page %page%)"
  economy: EXP
  fillItem:
    material: BLACK_STAINED_GLASS_PANE
    name: " "
  items:
    1:
      type: item
      item:
        material: LEATHER_HELMET
        quantity: 1
      buyPrice: 40
      sellPrice: 8
      slot: 10
Make sure all of used economies are enabled in config.yml:

economyTypes:
  - VAULT
  - EXP
Setting per-shop click actions
You can override the default click actions from config.yml (so e.g. LMB sells items and RMB buys them) by setting the same config entries in a shop.

Note: It overrides specified actions only. If you want to disable an action from config.yml, you have to set it to none.

Example:

armor:
  name: "&4&lArmor (page %page%)"
  clickActions:
    LEFT: SELL
    RIGHT: BUY
  items:
    1:
      type: item
      item:
        material: LEATHER_HELMET
        quantity: 1
      buyPrice: 40
      sellPrice: 8
      slot: 10
This results in left and right clicks being overridden, while middle click is still inherited from config.yml.
