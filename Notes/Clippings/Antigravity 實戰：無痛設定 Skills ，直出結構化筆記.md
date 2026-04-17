---
title: "Antigravity 實戰：無痛設定 Skills ，直出結構化筆記"
source: "https://www.youtube.com/watch?v=M9DYCKov9IM"
author:
  - "[[Paula 寶拉]]"
published: 2026-03-01
created: 2026-04-17
description: "這集我們來聊聊怎麼用 Skill 讓 AI 學會使用 Obsidian 的功能。AI 幫你整理的筆記，結構沒問題，但格式就只是最基本的 Markdown，因為它根本不知道你在用什麼工具。Skill 就是一份教學文件，告訴 AI 你的工具有哪些特殊語法跟功能，寫一次、放在固定位置，之後 AI 就會自動按照正確的方式輸出。從 Skills Marketplace 找到現成的 Obsidian"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=M9DYCKov9IM)

這集我們來聊聊怎麼用 Skill 讓 AI 學會使用 Obsidian 的功能。  
  
AI 幫你整理的筆記，結構沒問題，但格式就只是最基本的 Markdown，因為它根本不知道你在用什麼工具。Skill 就是一份教學文件，告訴 AI 你的工具有哪些特殊語法跟功能，寫一次、放在固定位置，之後 AI 就會自動按照正確的方式輸出。  
  
從 Skills Marketplace 找到現成的 Obsidian Markdown Skill，到實際安裝設定，再到前後對比，一步步帶你看有 Skill 跟沒有 Skill 的差異。  
  
(00:00) 前情回顧  
(00:27) 問題：AI 不認識你的工具  
(00:42) 什麼是 Skill？  
(02:37) 建立 Obsidian Markdown Skill  
(04:57) 有 Skill 後，AI 整理同一份會議記錄的結果  
(06:07) 差異一：Callout 標示重要提醒  
(07:09) 差異二：可互動的 Task List  
(07:52) 差異三：結構化的 FrontMatter  
(08:46) 重點回顧與自訂 Skill 的方法  
  
Skills Marketplace: https://skillsmp.com/  
Antigravity: https://antigravity.google/  
Obsidian: https://obsidian.md/

## Transcript

**0:00** · 上一集我們一起裝好了 Antigravity 跟 Obsidian 用 AI 產生筆記架構跟每日筆記模板 整個系統已經可以開始運作了，還沒看過的話，建議可以先回去看一下 這樣會延續上次的進度繼續 如果還沒訂閱的話，也請幫我按下訂閱 但你有沒有發現，AI 產生出來的內容結構是對的 可是格式就只是最基本的 markdown 語法 明明 Obsidian 有很多好用的功能，可是 AI 就是不會用 因為它根本不知道你在使用什麼樣的工具 今天我們就來解決這個問題 簡單來說，Skill 就是一份教學文件 告訴 AI 你用的工具有哪些特殊的語法跟功能 你寫一次，放在固定的位置 之後每次 AI 幫你處理相關的任務 它就會先讀這份文件，然後用正確的方式輸出 好，那我們先來看看，在沒有 Skill 的情況下，讓 AI 整理一篇文章會變成什麼樣 這是一份同步的會議記錄 原始的內容大概是誰說了什麼 目前卡在哪裡，接下來還有什麼要做，很標準的一個會議記錄 那我直接丟給 AI 跟他說，請幫我整理這份會議記錄並存成另外一個檔案 那我們回到 Antigravity 的畫面 那我這邊使用的是 Claude 的模型 好，結果出來了，我們到這個資料夾下看一下 那我們同一份檔案我們回到 Obsidian 看一下 那內容是沒有問題，結構也算清楚 但問題是它沒有使用任何 Obsidian 的功能 它只是用了最基本的 Markdown 在寫 那 Obsidian 那些好用的功能一個都沒有使用到 因為它根本不知道我們使用的是 Obsidian 如果你只是要一份 Markdown 文件，那這就足夠了 但如果你是想要在 Obsidian 裡面工作 這一格式就等於白白浪費了 Obsidian 的能力 等一下我會做一個詳細的前後對比，讓你更清楚差異在哪裡 好，那我們來看看怎麼樣設定 Skill 其實你不需要自己從 0 到 1 開始寫，有個網站叫做 Skills Marketplace 相關的網址我都會放在底下的資訊欄 那這個網站呢，它是一個開放的 Skill 市集 上面目前收錄超過 28 萬個 Skill 全部都是從 Github 上開源的專案 你可以把它想像成是一個 AI 技能商店 只是這邊賣的不是 APP，而是教 AI 認識各種工具的文件 那怎麼樣可以找到你想要的 Skills 呢 那它上面有個 AI 語意搜尋 那你不需要很清楚的知道技術名稱 只要直接打就可以了 比如說你想要搜尋 obsidian 相關的東西，那它就會列出相關的 skills 那我們在這邊搜尋 obsidian 那可以看到它顯示的都是 Obsidian 相關的搜尋結果 那我今天想要用來 demo 的是這個 Obsidian Markdown 那我們就點擊它 那我們可以看到這個 Skills 呢 它在底下列出的所有的功能 它其實都列的非常的清楚 那就是作為這次主要 demo 的範本 那我們這邊就點擊這個選項 然後我們就會進到這個 GitHub 畫面 然後我們再點擊 skill.md，然後可以看到這邊的內容就是跟剛剛在 Skills Marketplace 的內容是一樣的 那我們這邊就點擊 Code，然後在最右側點選 Copy，把這一份 Skill 複製下來 那我們就回到 Antigravity 的畫面 那我們在這個地方新增一個.agent 的資料夾 那我們在.agent 裡面再新增一個 skills 的資料夾 然後在這個資料夾底下，我們再新增一個資料夾 我們這邊就叫 obsidian-markdown 然後在這個資料夾， 我們再新增 skills.md 檔 然後把剛剛複製的內容貼上 那我們來看一下 skills.md 檔的內容 那你可以看到整個檔案呢， 分成兩個部分 一個部分是由這個 6 個減號組成的欄位， 然後另外一個部分是 markdown 組成的 那我們先來看一下這個上面六個減號組成的欄位呢 我們會叫它 YAML FrontMatter，也就是這個 Skills 的 Metadata，那它有兩個欄位 一個是 Name，一個是 Description，那 Name 的欄位呢，它就是這個 Skill 的名稱 那 Description 就是給 AI 看的說明，讓 AI 知道你這個 Skills 它是在做什麼 那什麼時候該使用它 那第二個部分就是以下這些由 Markdown 組成的正文 那這就是真正要教學 AI 的內容 那它的語法規則跟使用範例都顯示在這邊 那 Skills 的設定就到這邊，不需要額外安裝什麼內容或是跑什麼指令 只要放在對的位置就可以 AI 在處理 Markdown 相關的檔案的時候 它就會自動偵測到這份 Skills 按照裡面的內容來輸出 好，現在我們有了 Obsidian Skill，再來請 AI 幫我們整理同一份會議記錄 那就下一樣的指令，然後選擇一樣的 Claude 模型 然後可以看到說它這邊就有讀取到剛剛加入的這個 Skills 然後它一樣放在這個 01 的資料夾之中 大家可以看到 說在上面這個有會議記錄這個名稱的是在還沒有使用 Skills 的舊版本 那現在這個沒有會議記錄的是新的版本 那我們一樣就按 Accept All 好，那我們現在回到 Obsidian 看一下這兩份檔案的差異 好，左邊這個呢，是還沒有 Skill 的時候 AI 幫我整理的內容 那右邊呢，是使用 Skill 之後，它幫我整理的內容 那我們可以來看一下 那可以看到說，這次的結果不太一樣 那那些 Obsidian 的功能呢，AI 都有自動幫我使用上 那同樣的輸入，同樣的指定 差別在於說有沒有給 AI 那一份 Skills 最後我們來看一個比較完整的對比 瞭解有 skill 跟沒有 skill 的差異 第一個差異我們來看重要的提醒它是怎麼標的 我們先看原本的會議記錄 那我們這邊有說，Backend 說欄位可能會改名，然後有說應該不會改 那這邊有標示可能是應該 那我們來看沒有 Skills 的時候，AI 是怎麼幫我整理的 那可以看到說，它把它列在這邊 那這邊其實沒有什麼問題 但是它就只是一個符號，然後混合在整個條列裡面 它不是特別的突出，然後我們來看 Skills 它是怎麼幫我整理的 同樣的風險，AI 幫我改用了這個語法，就是這個 Warning 這是 Obsidian 的一個 Callout，就是你在 Obsidian 裡面打開這個筆記的時候 它會顯示成另外一個獨立的警告區塊，有圖示、有顏色 跟周圍的文字視覺上是完全分開的 重點不只是好看，而是你的眼睛在快速瀏覽這個筆記的時候會立刻被它吸引 這個就是 Callout 的核心價值 第二個差異是代辦事項，那我們可以來看，在沒有 Skills 的時候 它的代辦事項是一個表格，那這份資訊是完整的 只是它是靜態的，你只能看，沒有辦法做任何的動作 那我們可以來看有 Skills 的時候，它是改成 Obsidian 的這個 Task List 你在 Obsidian 裡面打開，每一行前面都有一個可以勾選的方框 完成了之後你就直接打勾 那重點是說你不需要在開完會之後 再把這個 Action Item 複製到另外一個地方管理 那這份筆記本身就是你的清單 看完會之後就可以開始直接運作 那這就是有 skill 跟沒有 skill 的最大的差別 在沒有 skill 的時候，AI 不知道 obsidian 有這個功能，所以它不會用 那有 skill 的時候，它就會把這個工具的語法放在適合的地方去主動的使用它 那第三個差異，有無結構化的 frontmatter 那我們可以滑到最上面的時候來比對一下 在這個左邊的沒有 skill 的版本，它就是直接從標題開始 連 frontmatter 都沒有，沒有日期、沒有 tag、沒有 status，就是一份純文字的 markdown 但有 skills 的版本呢，它上面就是多了這一段 那這個是 obsidian 的屬性，那也就是筆記的 metadata，有了這個之後 你可以使用更多 obsidian 的進階功能，像是 data view 或是搜尋 直接過濾所有 status 是 action required 的筆記 那這個月所有 Meeting 的紀錄也可以直接一起做過濾 但這些都是需要有結構化的資料才可以做到的 如果你不告訴 AI，它不知道 Obsidian 有這個地方可以放這些 Metadata 所以它根本就不會去加 但有了 Skills 之後，AI 知道這個格式的存在 也就可以在產出筆記的時候自動幫你填好 那我們來回顧一下今天的重點 Skill 其實就是一份教學文件 放在固定的位置，讓 AI 知道你要用什麼工具，有哪些工具可以使用 設定的方式也很簡單，就是在點 Agent-Skills 底下的資料夾，新增你想要使用的 Skill 有了它之後，AI 就不再只是會寫基本的 Markdown 而是會主動幫你使用 Callout 標重點 在筆記內加上這個結構化的 FrontMatter 那這些本來就是工具的功能 只是我們一開始沒有告訴 AI 如果你今天想要新增其他內容 我們一樣就是在 Skills 的這個資料夾底下 新增另外一個資料夾 然後使用 skills.md 檔，那一樣就可以寫上你想要的內容 那一樣要按照著我們這個 skill 的格式，在前面加上 metadata 然後後面加上你的描述，那你就可以寫出自己的 skills 那今天的這一集就到這邊 如果你有興趣想要聽別的主題 也歡迎在底下留言告訴我 那記得按讚訂閱開啟小鈴鐺 我們下次見