# Publish AIPartner for Facebook

Human HTML guide: FACEBOOK_PUBLISHING.html

## The important correction

Do not select or open index.html to publish the website.

The Code page is used only to confirm that index.html exists at the top level of the repository.
GitHub Pages publishes a branch and folder, not one selected file.

For AIPartner, the required publishing source is:

- Branch: main
- Folder: /(root)

## Part 1: Confirm the file is on GitHub

1. Open:
   https://github.com/imtoam/AIPartner
2. Select Code if the repository file list is not already visible.
3. Confirm that index.html appears in the first level of the file list.
4. Do not open index.html.
5. Continue to Part 2.

If index.html is missing from the GitHub file list, return to GitHub Desktop, commit the local
changes, select Push origin, and refresh the repository page.

## Part 2: Enable GitHub Pages

Starting from the AIPartner repository page:

1. Select Settings in the repository navigation near the top of the page.
2. If Settings is hidden, open the additional navigation menu and select Settings there.
3. In the left sidebar, find the Code and automation group.
4. Select Pages.
5. Find the Build and deployment section.
6. In the Source menu, select Deploy from a branch.
7. A branch row will appear below Source.
8. In the first menu of that row, select main.
9. In the second menu, select /(root).
10. Select Save.

Do not select GitHub Actions as the Source. This static website does not need a custom workflow.

The final settings must read:

Source: Deploy from a branch

Branch: main

Folder: /(root)

## Part 3: Wait for publication

After selecting Save:

1. Stay on the Pages settings screen.
2. GitHub will start a Pages deployment.
3. Wait for the message that the site is live. The first deployment may take several minutes.
4. Open:
   https://imtoam.github.io/AIPartner/

The root address should display the visual human starting guide.

The English article address is:

https://imtoam.github.io/AIPartner/introduction/ai-native-project.html

The French article address is:

https://imtoam.github.io/AIPartner/introduction/ai-native-project-fr.html

The French page will not exist online until ai-native-project-fr.html has been committed and pushed.

## If the Pages screen does not look right

### Settings is missing

Open the additional repository navigation menu. If Settings is still absent, confirm that you are
signed into the repository owner account and have administrator permission.

### Pages is missing

Look in the left sidebar under Code and automation. If the repository is private and the current
GitHub plan does not support Pages for private repositories, make the repository public or use a
plan that supports private Pages.

### The branch menu says None

Open it and select main. If main does not appear, confirm that the local commit was pushed to
GitHub.

### Save is disabled

The same publishing source may already be saved. Check whether the screen already shows main and
/(root), then look near the top of the Pages screen for the published site address.

### The site shows 404

Check these items:

1. Wait several minutes and refresh.
2. Confirm the Pages source is main and /(root).
3. Confirm index.html is visible at the repository root under Code.
4. Open the Actions tab and look for the latest pages build and deployment run.
5. A green result means deployment completed.
6. A red result can be opened to show the failed step.

The filename must be exactly index.html. Capitalization matters.

### The root guide works but an article does not

Confirm that the article file is visible in the introduction directory on GitHub. A file that
exists only on the computer cannot be published until it is committed and pushed.

## Publish the Facebook post

Only continue after the selected article opens through its github.io address.

1. Open facebook-post.md.
2. Choose EN or FR.
3. Choose the recommended or short version.
4. Copy the text and its matching article URL into Facebook.
5. Wait for Facebook to display the preview.
6. Confirm the title and image before publishing.

If Facebook shows an older preview, submit the selected article URL to the Facebook Sharing
Debugger and request a new scrape.

## The two GitHub surfaces

Repository:

https://github.com/imtoam/AIPartner

Use it to manage files, commits, settings, and deployment status.

Published website:

https://imtoam.github.io/AIPartner/

Use it for human reading and Facebook links.
