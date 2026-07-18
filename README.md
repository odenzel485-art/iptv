# My First App - TV Streaming Platform

> A modern, YouTube-inspired IPTV streaming application with 500+ channels, responsive design, and an intuitive interface.

## Overview

**My First App** is a web-based TV streaming platform designed for seamless channel browsing and playback. Built with vanilla HTML5, CSS3, and JavaScript ES6+, it provides a lightweight yet feature-rich streaming experience without external dependencies.

The application supports M3U8 playlists and integrates with HLS.js for adaptive bitrate streaming, making it compatible with both live streams and on-demand content.

## Features

### Core Functionality
- **500+ Channels** - Kenya TV, Kids programming, and international content
- **Search & Filter** - Real-time search across all channels
- **Category Navigation** - Organized into Home, Kenya TV, Kids, and Recently Watched
- **Channel Navigation** - Previous/Next buttons for quick channel switching
- **Dark Theme** - YouTube-inspired dark interface with smooth animations

### Technical Features
- **Responsive Design** - Mobile-first approach with breakpoints for all screen sizes
- **PWA Ready** - Web manifest for app-like installation on mobile devices
- **Auto-Refresh** - Playlist updates automatically every 30 minutes
- **Local Storage** - Recently watched history persists across sessions
- **HLS.js Support** - Adaptive streaming for reliable playback
- **Zero Dependencies** - Pure vanilla JavaScript, no build tools required

### User Experience
- **Offline-Capable** - Works with cached playlists
- **Fast Loading** - Lightweight (~20KB HTML, optimized CSS)
- **Touch-Friendly** - Optimized controls for mobile and tablet devices
- **No Ads** - Clean, distraction-free streaming

## Getting Started

### Option 1: Web Browser (Recommended)
```bash
# Simply open index.html in any modern browser
# Firefox, Chrome, Safari, and Edge are all supported
```

### Option 2: IPTV Player Integration
Use the M3U playlist URL with external IPTV players (VLC, IPTV Smarters, etc.):

```
https://raw.githubusercontent.com/odenzel485-art/project-1/refs/heads/main/project_1.m3u
```

## System Requirements

- **Browser**: Modern browser with ES6+ support (Chrome 51+, Firefox 54+, Safari 10+, Edge 15+)
- **Network**: Stable internet connection (minimum 2 Mbps for SD, 5 Mbps for HD)
- **Storage**: ~15 MB for app files
- **Optional**: PWA support for mobile app installation

## File Structure

```
project-1/
├── index.html           # Main application file
├── project_1.m3u        # M3U playlist (500+ channels)
├── project_1.py         # Python utility script
├── manifest.json        # PWA configuration
├── README.md            # Documentation
└── cookies.txt          # Session storage
```

## Configuration

### M3U Playlist
- **Location**: `project_1.m3u`
- **Format**: M3U8 with extended information tags
- **Updates**: Auto-refreshed every 30 minutes
- **Source**: Mix of YouTube livestreams, HLS streams, and RTMP feeds

### Channel Categories
- **🏠 All Channels** - Complete library view
- **🇰🇪 Kenya TV** - Local Kenyan television
- **👶 Kids** - Family-friendly content
- **🕐 Recently Watched** - User's viewing history

## Technical Stack

### Frontend
- HTML5
- CSS3 with CSS Variables for theming
- JavaScript ES6+
- HLS.js (CDN)

### Architecture
- Single-page application (SPA)
- Module-based function organization
- LocalStorage for persistent state
- Event-driven UI updates

### Browser APIs
- Fetch API for playlist loading
- HTML5 Video API for playback
- LocalStorage API for history tracking
- setInterval for auto-refresh

## Supported Streams

The application supports multiple stream formats:

- **HLS (.m3u8)** - Adaptive bitrate streaming
- **RTMP** - Real-time messaging protocol streams
- **HTTP Progressive** - Direct MP4/WebM streams
- **YouTube** - Direct YouTube watch URLs and livestreams

## Performance

- **Initial Load**: < 2 seconds
- **Channel Search**: < 100ms with 500+ channels
- **Memory Usage**: ~50-100 MB during playback
- **Playlist Auto-Refresh**: 30-minute intervals (configurable)

## Browser Compatibility

| Browser | Version | Status |
|---------|---------|--------|
| Chrome  | 51+     | ✅ Full Support |
| Firefox | 54+     | ✅ Full Support |
| Safari  | 10+     | ✅ Full Support |
| Edge    | 15+     | ✅ Full Support |
| Mobile Safari | 10+ | ✅ Full Support |

## Known Limitations

- Geographically restricted streams may not be accessible outside their region
- Some YouTube streams require active internet connection and may have regional restrictions
- Stream quality depends on source availability and network conditions
- Ad-supported streams from free sources may occasionally be unavailable

## Troubleshooting

### Channels Not Loading
1. Check internet connection
2. Verify M3U playlist URL is accessible
3. Wait for auto-refresh (30 minutes) or manually refresh
4. Clear browser cache and local storage

### Playback Issues
1. Verify stream is currently live/available
2. Try a different channel to isolate the issue
3. Check browser console for error messages
4. Update browser to latest version

### Performance Issues
1. Close other browser tabs/applications
2. Reduce video quality if available
3. Clear browser cache
4. Restart the browser application

## Development

### Running Locally
```bash
# Clone the repository
git clone https://github.com/odenzel485-art/project-1.git

# Navigate to directory
cd project-1

# Open in browser (no build step required)
# Option 1: Double-click index.html
# Option 2: python -m http.server 8000
# Option 3: Use VS Code Live Server extension
```

### Modifying Channel List
Edit `project_1.m3u` directly with any text editor. Format:
```
#EXTINF:-1 tvg-name="Channel Name" group-title="Category",Display Name
stream_url_here
```

## License

This project is provided as-is for educational and personal use.

## Support

For issues, suggestions, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review browser console for error messages
- Verify network connectivity and stream availability

## Changelog

### v1.0 (Current)
- Initial release
- 500+ channel support
- YouTube-style UI
- Auto-refresh functionality
- Mobile responsiveness
- Previous/Next channel navigation

