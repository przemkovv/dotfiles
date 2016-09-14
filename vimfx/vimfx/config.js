let map = (shortcuts, command, custom=false) => {
      vimfx.set(`${custom ? 'custom.' : ''}mode.normal.${command}`, shortcuts)
}
let {commands} = vimfx.modes.normal

vimfx.addCommand({
    name: 'search_tabs',
    description: 'Search tabs',
    category: 'location',
    order: commands.focus_location_bar.order + 1,
}, (args) => {
    commands.focus_location_bar.run(args)
    args.vim.window.gURLBar.value = '% '
})
map('b', 'search_tabs', true)

vimfx.addCommand({
  name: 'tab_close_to_left',
  description: 'Close tabs to the left',
  category: 'tabs',
  order: commands.tab_close_to_end.order + 1,
}, (args) => {
  commands.tab_close.run(args)
  commands.tab_select_previous.run(args)
})
map('D', 'tab_close_to_left', true)

vimfx.addCommand({
    name: 'zoom_out',
      description: 'Zoom out',
}, ({vim, count}) => {
  for (let i = 0; i < count; i++){
    vim.window.FullZoom.reduce()
  }
})
map('zo zO', 'zoom_out', true)
vimfx.addCommand({
    name: 'zoom_in',
      description: 'Zoom in',
}, ({vim, count}) => {
  for (let i = 0; i < count; i++){
    vim.window.FullZoom.enlarge()
  }
})
map('zi zI', 'zoom_in', true)
vimfx.addCommand({
    name: 'zoom_reset',
      description: 'Zoom reset',
}, ({vim}) => {
    vim.window.FullZoom.reset()
})
map('zz', 'zoom_reset', true)


vimfx.set('hint_chars', 'asdfghjklqweriop')
map('J', 'scroll_half_page_down')
map('K', 'scroll_half_page_up')
map('', 'scroll_left')
map('', 'scroll_right')
map('d', 'tab_close')
map('u', 'tab_restore')
map('l gt', 'tab_select_next')
map('h gT', 'tab_select_previous')
vimfx.set('prevent_autofocus', true)

