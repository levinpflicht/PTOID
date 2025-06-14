(async () => {
  const openModule = await import('open');
  await openModule.default('https://www.youtube.com/watch?v=dQw4w9WgXcQ');
})();
