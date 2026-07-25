# Publishing the Article for Facebook

## Recommended approach

Host the article as a public static webpage and share its HTTPS address in Facebook.

Facebook does not reproduce the custom HTML and CSS inside a normal post. The post provides the introduction and link preview. When a reader selects the link, Facebook opens the full webpage in its in-app browser or the reader's external browser.

GitHub Pages is a good host for this article because the page is static and does not require a server, database, login, or build system.

## Do not publish the whole working repository

Use a separate public repository for the article unless every file in the current project is already intended to be public.

Publishing the entire working repository can expose source code, configuration, project history, internal documentation, or other material unrelated to the article. The publishing repository should contain only the files needed by the public page.

## Files to publish

Copy these files into the root of the publishing repository:

- ai-native-project.html
- facebook-share-card.png

Rename ai-native-project.html to index.html. The published repository root should then look like this:

    index.html
    facebook-share-card.png

The SVG source can also be included if desired:

    facebook-share-card.svg

The Facebook post copy and this guide do not need to be published with the website.

## Create the GitHub Pages site

1. Create a new public GitHub repository. A clear name such as human-ai-software works well.
2. Add index.html and facebook-share-card.png to the repository root.
3. Open the repository Settings page.
4. Select Pages under Code and automation.
5. Under Build and deployment, choose Deploy from a branch.
6. Select the main branch and the root folder.
7. Save and wait for GitHub to display the public site address.

For a project repository, the default address normally has this form:

    https://GITHUB_USERNAME.github.io/REPOSITORY_NAME/

The article must be publicly reachable without a login because Facebook needs to fetch the page and its preview image.

## Configure the preview image

The article already contains Open Graph metadata for Facebook. Before publishing, change the og:image value in index.html from the relative filename to the final absolute HTTPS address.

For example:

    <meta property="og:image" content="https://GITHUB_USERNAME.github.io/REPOSITORY_NAME/facebook-share-card.png" />

An absolute address is safer for link preview crawlers than a relative address.

The article URL itself does not need to be hardcoded in the page. Facebook can use the address that was shared.

## Publish on Facebook

1. Open facebook-post.md.
2. Choose the recommended post or the short version.
3. Replace PUBLIC_ARTICLE_URL with the GitHub Pages address.
4. Paste the text into Facebook.
5. Wait for the link preview to appear.
6. Confirm that the title, description, and share card are correct.
7. Publish the post.

The reader selects the preview or URL and Facebook opens the full HTML article.

## If the preview is stale

Facebook may retain an earlier title, description, or image after the webpage changes. Confirm that the public page and image load without authentication, then ask Facebook to inspect the public URL again using its sharing debugger before publishing the final post.

## Optional custom domain

GitHub Pages can also use a custom domain. This is useful if the article becomes part of a continuing publication, but it is not required for the first release. The default github.io address is sufficient for a Facebook link.

## Alternative hosts

Cloudflare Pages, Netlify, and similar static hosts can serve the same two files. The requirements are the same:

- A public HTTPS article URL
- A public HTTPS preview image URL
- No login wall
- No dependency on local files

GitHub Pages is the simplest starting point when the article files are already managed with Git.
